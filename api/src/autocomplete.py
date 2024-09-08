from dotenv import load_dotenv
load_dotenv()

import nest_asyncio
nest_asyncio.apply()

from llama_parse import LlamaParse
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from llama_index.core import SummaryIndex
from llama_index.core import SimpleDirectoryReader
from llama_index.core import PromptTemplate
import json
from json import JSONDecodeError
import os
from pathlib import Path

class MySuperCoolLLM():
    data_path = (Path(__file__).parent / "data.xlsx").as_posix()
    model_name = "llama3.1"
    model_temperature = 0.9
    request_timeout = 180.0

    def __init__(self):

        parser = LlamaParse(result_type="markdown")
        file_extractor = {".xlsx": parser}
        documents = SimpleDirectoryReader(input_files=[self.data_path], file_extractor=file_extractor).load_data()
        base_index = SummaryIndex.from_documents(documents)

        Settings.llm = Ollama(
            model=self.model_name, request_timeout=self.request_timeout, temperature=self.model_temperature,
            base_url=os.environ.get("OLLAMA_BASE_PATH"))


        self.base_query_engine = base_index.as_query_engine(text_qa_template=self.autocomplete_template)

    @property
    def autocomplete_template(self):
        autocomplete_template_str = (
            "Context information is below.\n"
            "---------------------\n"
            "{context_str}\n"
            "---------------------\n"
            "You are helping users formulate the title of a decision they want to make given the context information."
            " Based on the user's input, suggest exactly 5 potential decision titles."
            " Return the suggestions as a list of strings that is JSON serializable, with no extra explanation or introduction."
            " if the query is empty, provide 5 output questions that are in your context information."
            " the suggestions must be short but never empty strings."
            "Query: {query_str}\n"
            "Answer: "
        )

        return PromptTemplate(autocomplete_template_str)

    def get_suggestions(self, user_input):
        response = self.base_query_engine.query(user_input)
        try:
            return json.loads(response.response)
        except JSONDecodeError:
            return []
