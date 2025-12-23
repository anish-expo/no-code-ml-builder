<template>
  <div class="card">
    <h3>1️.  Upload Dataset</h3>

    <input
      type="file"
      @change="upload"
      accept=".csv,.xlsx"
    />

    <p v-if="error" class="error">
      {{ error }}
    </p>

    <p v-if="info" class="success">
      Rows: {{ info.rows }} | Columns: {{ info.columns }}
    </p>

    <p v-if="info">
      <strong>Column Names:</strong> {{ info.column_names }}
    </p>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'

const emit = defineEmits(['uploaded'])

const info = ref(null)
const error = ref(null)

const upload = async (e) => {
  error.value = null
  info.value = null

  const file = e.target.files[0]
  if (!file) return

  const allowedTypes = [
    "text/csv",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
  ]

  if (!allowedTypes.includes(file.type)) {
    error.value = "Only CSV or Excel (.xlsx) files are allowed."
    return
  }

  const form = new FormData()
  form.append("file", file)

  try {
    const res = await axios.post(
      "https://no-code-ml-builder-e7q4.onrender.com/upload",
      form
    )
    info.value = res.data
    emit("uploaded", res.data.column_names)
  } catch (err) {
    error.value =
      err.response?.data?.error ||
      "Upload failed. Please try again."
  }
}
</script>

<style scoped>
@import '../main.css';

.info {
  margin-top: 10px;
  color: #2b6cb0;
  font-weight: 500;
}
.error {
  color: #dc2626;
  font-weight: 600;
  margin-top: 8px;
}

.success {
  color: #16a34a;
  font-weight: 600;
  margin-top: 8px;
}
</style>