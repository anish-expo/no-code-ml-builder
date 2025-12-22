<!-- <template>
  <div class="card" v-if="results">
    <h3>5️. Results</h3>

    <p class="model-name">
      Model Used: <strong>{{ results.model }}</strong>
    </p>

    <p class="accuracy">
      Accuracy: {{ (results.accuracy * 100).toFixed(2) }}%
    </p>

    <h4>Confusion Matrix</h4>

    <div class="matrix">
      <div class="cell header"></div>
      <div class="cell header">Predicted 0</div>
      <div class="cell header">Predicted 1</div>

      <div class="cell header">Actual 0</div>
      <div class="cell success">
        {{ results.confusion_matrix[0][0] }}
      </div>
      <div class="cell error">
        {{ results.confusion_matrix[0][1] }}
      </div>

      <div class="cell header">Actual 1</div>
      <div class="cell error">
        {{ results.confusion_matrix[1][0] }}
      </div>
      <div class="cell success">
        {{ results.confusion_matrix[1][1] }}
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  results: Object
})
</script> -->

<template>
  <div class="card" v-if="results">
    <h3>5️. Results</h3>

    <p><strong>Model Used:</strong> {{ results.model }}</p>

    <p class="accuracy">
      Accuracy: {{ (results.accuracy * 100).toFixed(2) }}%
    </p>

    <h4>Confusion Matrix</h4>

    <div class="matrix">
      <div class="cell header"></div>
      <div class="cell header">
        Predicted: {{ className(results.class_labels[0]) }}
      </div>
      <div class="cell header">
        Predicted: {{ className(results.class_labels[1]) }}
      </div>

      <div class="cell header">
        Actual: {{ className(results.class_labels[0]) }}
      </div>
      <div class="cell success">
        {{ results.confusion_matrix[0][0] }}
      </div>
      <div class="cell error">
        {{ results.confusion_matrix[0][1] }}
      </div>

      <div class="cell header">
        Actual: {{ className(results.class_labels[1]) }}
      </div>
      <div class="cell error">
        {{ results.confusion_matrix[1][0] }}
      </div>
      <div class="cell success">
        {{ results.confusion_matrix[1][1] }}
      </div>
    </div>

    <p class="note">
      🟩 Correct Predictions &nbsp;&nbsp; 🟥 Incorrect Predictions
    </p>
  </div>
</template>

<script setup>
defineProps({
  results: Object
})

const className = (label) => {
  if (label === 0) return "No Disease"
  if (label === 1) return "Disease"
  return label
}
</script>


<style scoped>
.card {
  background: white;
  padding: 24px;
  border-radius: 14px;
  box-shadow: 0 12px 30px rgba(0,0,0,0.06);
}

.model-name {
  font-size: 16px;
  margin-bottom: 10px;
}

.accuracy {
  font-size: 20px;
  font-weight: bold;
  color: #16a34a;
  margin-bottom: 20px;
}

.matrix {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  max-width: 350px;
}

.cell {
  padding: 14px;
  text-align: center;
  border-radius: 8px;
  font-weight: 600;
}

.header {
  background: #f1f5f9;
  font-weight: bold;
}

.success {
  background: #dcfce7;
  color: #166534;
}

.error {
  background: #fee2e2;
  color: #991b1b;
}
</style>