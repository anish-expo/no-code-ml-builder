<template>
  <div class="card">
    <h3>3️.  Train-Test Split</h3>
    <select v-model="ratio">
      <option :value="0.7">70-30</option>
      <option :value="0.8">80-20</option>
    </select>
    <button @click="split">Apply Split</button>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'

const ratio = ref(0.8)
const emit = defineEmits(['splitted'])

const split = async () => {
  await axios.post("https://no-code-ml-builder-e7q4.onrender.com/split", { ratio: ratio.value })
  alert("Split Done")
  emit("splitted") 
}
</script>

<style scoped>
@import '../main.css';

select, button {
  padding: 10px;
  border-radius: 8px;
}
button {
  background: #10b981;
  color: white;
  border: none;
}
</style>
