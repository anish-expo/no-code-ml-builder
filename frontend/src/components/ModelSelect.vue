<template>
  <div class="card">
    <h3>4️. Model Selection</h3>
    <div class="actions">
      <button @click="train('logistic')">Logistic Regression</button>
      <button @click="train('tree')">Decision Tree</button>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'

const emit = defineEmits(['trained'])

const train = async (model) => {
  const res = await axios.post("http://localhost:5000/train", { model })
  emit("trained", res.data)
}
</script>

<style scoped>
@import '../main.css';

.actions {
  display: flex;
  gap: 12px;
}

button {
  padding: 12px;
  border-radius: 10px;
  border: none;
  background: #2563eb;
  color: white;
  cursor: pointer;
}
</style>