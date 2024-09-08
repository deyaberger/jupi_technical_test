<script setup>
import { useRoute, useRouter } from 'vue-router'
const route = useRoute()
const router = useRouter()
const suggestionName = route.params.name


const goHome = (suggestion) => {
  router.push({ name: 'home'})
}
</script>


<template>
  <div class="suggestion-page">
    <h1>{{ suggestionName }}
    </h1>
    <a @click="goHome">Go Home</a>
</div>
</template>

<style>
.suggestion-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column; /* Stack elements vertically */
  align-items: center;
  justify-content: center; /* Center vertically */
}

h1 {
  margin-bottom: 20px; /* Add space between the title and button */
  font-size: 2.6rem;
  text-align: center;
  color: white;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
