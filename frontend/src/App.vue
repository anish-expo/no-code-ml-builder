<!-- <template>
  <div class="container">
    <h1>No-Code ML Pipeline Builder</h1>
    <p class="subtitle">
      Build a complete machine learning pipeline without writing code
    </p>

    <div class="pipeline">
      <DatasetUpload @uploaded="cols = $event" />
      <Preprocessing v-if="cols.length" :columns="cols" />
      <TrainTestSplit />
      <ModelSelect @trained="results = $event" />
      <Results :results="results" />
    </div>
  </div>
</template>

<script setup>
import DatasetUpload from './components/DatasetUpload.vue'
import Preprocessing from './components/Preprocessing.vue'
import TrainTestSplit from './components/TrainTestSplit.vue'
import ModelSelect from './components/ModelSelect.vue'
import Results from './components/Results.vue'

import { ref } from 'vue'
const cols = ref([])

const results = ref(null)
</script> -->

<template>
  <div class="container">
    <h1>No-Code ML Pipeline Builder</h1>
    <p class="subtitle">
      Build a complete machine learning pipeline without writing code
    </p>

    <!-- STEP 1: Upload -->
    <DatasetUpload @uploaded="onUploaded" />

    <!-- STEP 2: Preprocessing -->
    <Preprocessing
      v-if="step >= 2"
      :columns="columns"
      @preprocessed="onPreprocessed"
    />

    <!-- STEP 3: Train-Test Split -->
    <TrainTestSplit
      v-if="step >= 3"
      @splitted="onSplitted"
    />

    <!-- STEP 4: Model Selection -->
    <ModelSelect
      v-if="step >= 4"
      @trained="onTrained"
    />

    <!-- STEP 5: Results -->
    <Results
      v-if="step >= 5"
      :results="results"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'

import DatasetUpload from './components/DatasetUpload.vue'
import Preprocessing from './components/Preprocessing.vue'
import TrainTestSplit from './components/TrainTestSplit.vue'
import ModelSelect from './components/ModelSelect.vue'
import Results from './components/Results.vue'

const step = ref(1)
const columns = ref([])
const results = ref(null)

const onUploaded = (cols) => {
  columns.value = cols
  step.value = 2
}

const onPreprocessed = () => {
  step.value = 3
}

const onSplitted = () => {
  step.value = 4
}

const onTrained = (res) => {
  results.value = res
  step.value = 5
}
</script>

<style scoped>
.container {
  max-width: 900px;
  margin: auto;
  padding: 40px 20px;
}

h1 {
  text-align: center;
  font-size: 32px;
  margin-bottom: 5px;
}

.subtitle {
  text-align: center;
  color: #666;
  margin-bottom: 40px;
}

.pipeline {
  display: grid;
  gap: 20px;
}
</style>
