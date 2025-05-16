<template>
  <div class="thread-write-container">
    <h1>AI 피드백 전후 비교</h1>

    <!-- 입력 폼 -->
    <label>제목:</label>
    <input v-model="title" type="text" placeholder="제목을 입력하세요" />

    <label>내용:</label>
    <textarea v-model="content" placeholder="내용을 입력하세요"></textarea>

    <button @click="getAiFeedback">AI 피드백 요청</button>

    <!-- AI 피드백 진행 상태 -->
    <div v-if="isLoading">AI 피드백 진행 중...</div>

    <!-- AI 피드백 결과 -->
    <div v-if="aiFeedback" class="feedback-container">
      <h3>AI 피드백 결과</h3>
      <p>{{ aiFeedback }}</p>
    </div>

    <!-- AI 변경점 비교 -->
    <div v-if="diffResult.length" class="diff-container">
      <h3>AI 수정 전후 비교</h3>
      <p>
        <span v-for="part in diffResult" :key="part.value"
              :class="{ added: part.added, removed: part.removed }">
          {{ part.value }}
        </span>
      </p>
    </div>
  </div>
</template>
<script setup>
import { ref } from 'vue';
import axios from 'axios';
import * as Diff from 'diff';

const title = ref('');
const content = ref('');
const aiFeedback = ref(null);
const diffResult = ref([]);
const isLoading = ref(false);

// OpenAI API 호출
const getAiFeedback = async () => {
  isLoading.value = true;
  
  try {
    const response = await axios.post('https://api.openai.com/v1/completions', {
      model: 'text-davinci-003',
      prompt: `다음 글을 더 공손하고 유창하게 수정해 주세요:\n\n"${content.value}"`,
      max_tokens: 200,
      temperature: 0.7,
    }, {
      headers: {
        'Authorization': `Bearer ${import.meta.env.VITE_OPENAI_API_KEY}`,
        'Content-Type': 'application/json'
      }
    });

    aiFeedback.value = response.data.choices[0].text.trim();

    // Diff 비교
    diffResult.value = Diff.diffWords(content.value, aiFeedback.value);
  } catch (error) {
    console.error('AI 피드백 요청 실패:', error);
  } finally {
    isLoading.value = false;
  }
};
</script>


<style scoped>
.thread-write-container {
  padding: 20px;
}

.feedback-container, .diff-container {
  margin-top: 20px;
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
}

.added {
  background-color: #d4f5d4;
}

.removed {
  background-color: #f5d4d4;
  text-decoration: line-through;
}
</style>
