<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const query = ref('')
const suggestions = ref([])
const loading = ref(false)

const fetchSuggestions = async () => {
  if (query.value.length > 0) {
    loading.value = true
    try {
      const response = await fetch(`http://localhost:8000/suggestions/?query=${query.value}`)
      const data = await response.json()
      suggestions.value = data.suggestions
    } catch (error) {
      console.error('Error fetching suggestions:', error)
    } finally {
      loading.value = false // Stop loading
    }
  } else {
    suggestions.value = []
  }
}

const router = useRouter()
const goToSuggestionPage = (suggestion) => {
  router.push({ name: 'Suggestion', params: { name: suggestion } })
}
</script>

<template>
  <img alt="Vue logo" class="logo" src="@/assets/logo.png" width="125" height="125" />
  <div class="greetings">
    <h1 class="blue">Help us guide you in your decision making process</h1>
    <h3>
      Type in the question you need to answer:
    </h3>
    <div>
      <div class="search-container">
      <input v-model="query" @input="fetchSuggestions" placeholder="Search..."/>
      <div class="suggestions" v-if="query.length > 0">
        <div v-if="loading" class="loading">
          <v-progress-circular
          class="loading-circle"
          indeterminate
          color="primary"
          size="32"
          :rotate="360"
        ></v-progress-circular>
        </div>
        <div v-else>
          <div v-for="suggestion in suggestions" :key="suggestion" class="suggestion-item"
            @click="goToSuggestionPage(suggestion)">
              <p>{{ suggestion }}</p>
            </div>
        </div>
    </div>
    </div>
    </div>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.5rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.5rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: cneter;
  }
}

.search-container {
  width: 80%;
  margin: 20px auto;
  position: relative;
}

input {
  width: 100%;
  padding: 15px;
  border-radius: 10px 10px 10px 10px;
  border: 1px solid #ccc;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  background-color: white;
  font-size: 1.1rem;
  box-sizing: border-box;
  outline: none;
}

.loading-circle {
  margin: 5px 5px;
  animation-duration: 3s;
}


.suggestions {
  position: absolute;
  width: 100%;
  background-color: white;
  border-radius: 0px 0px 10px 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  z-index: 10;
  margin-top: 5px;
}

.suggestion-item {
  display: flex;
  align-items: center;
  padding: 10px 15px;
  cursor: pointer;
  transition: background-color 0.2s ease-in-out;
}

.suggestion-item:hover {
  background-color: #f1f1f1;
}

.suggestion-item p {
  margin-left: 10px;
  font-size: 1rem;
  color: #333;
}

</style>
