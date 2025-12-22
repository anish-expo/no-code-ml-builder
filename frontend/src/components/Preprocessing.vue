<template>
  <div class="card">
    <h3>2️. Data Preprocessing</h3>

    <select v-model="target">
      <option disabled value="">Select Target Column</option>
      <option v-for="c in columns" :key="c">{{ c }}</option>
    </select>

    <div class="actions">
      <button class="primary" @click="apply('standardize')">
        Standardize
      </button>
      <button class="secondary" @click="apply('normalize')">
        Normalize
      </button>
    </div>

    
    <div v-if="summary" class="summary">
      <p class="success"> {{ summary.status }} and Scaling Method {{ summary.scaling_method }}</p>

      <p><strong>Numeric Features Scaled:</strong></p>
      <ul>
        <li v-for="n in summary.numeric_features" :key="n">
          {{ n }}
        </li>
      </ul>

      <p><strong>Categorical Features Encoded:</strong></p>
      <ul>
        <li v-for="c in summary.categorical_features" :key="c">
          {{ c }}
        </li>
      </ul>

      <p class="final-count">
        Final Feature Count: {{ summary.final_feature_count }}
      </p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'

defineProps({ columns: Array })

const target = ref("")
const summary = ref(null)

const emit = defineEmits(['preprocessed'])

const apply = async (method) => {
  const res = await axios.post("http://localhost:5000/preprocess", {
    method,
    target: target.value
  })

  summary.value = res.data
  emit("preprocessed")
}
</script>

<style scoped>
@import '../main.css';

select {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border-radius: 8px;
  border: 1px solid #ccc;
}

.actions {
  display: flex;
  gap: 10px;
  margin-bottom: 15px;
}

button {
  padding: 10px 16px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
}

.primary {
  background: #4f46e5;
  color: white;
}

.secondary {
  background: #e0e7ff;
}

.summary {
  margin-top: 20px;
  padding: 15px;
  background: #f8fafc;
  border-radius: 10px;
  font-size: 14px;
}

.success {
  color: #16a34a;
  font-weight: bold;
}

ul {
  padding-left: 20px;
  margin-top: 5px;
}

.final-count {
  margin-top: 10px;
  font-weight: bold;
  color: #1d4ed8;
}
</style>