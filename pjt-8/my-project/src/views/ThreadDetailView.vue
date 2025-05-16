<template>
  <div v-if="loading">로딩 중...</div>

  <div v-else-if="thread" class="thread-detail-container">
    <h1>{{ thread.title }}</h1>
    <p><strong>작성일:</strong> {{ thread.date }}</p>
    <p><strong>카테고리:</strong> {{ thread.category }}</p>
    <div class="thread-content">
      <p>{{ thread.content }}</p>
    </div>
  </div>

  <div v-else class="not-found">
    <p>해당 스레드를 찾을 수 없습니다.</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

// 현재 라우트에서 threadId 추출
const route = useRoute()
const threadId = parseInt(route.params.threadId)

const thread = ref(null)
const loading = ref(true)

onMounted(async () => {
  try {
    // 비동기로 로컬스토리지에서 스레드 목록 불러오기
    const stored = localStorage.getItem('threads')
    const parsed = stored ? JSON.parse(stored) : []

    // 해당 threadId를 가진 스레드 찾기
    const found = parsed.find(t => t.id === threadId)

    // 비동기 시뮬레이션 (예: 서버 요청이 있는 경우)
    await new Promise(resolve => setTimeout(resolve, 300)) // 300ms 지연

    thread.value = found
  } catch (err) {
    console.error('스레드 로드 중 오류:', err)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.thread-detail-container {
  padding: 20px;
}
.thread-content {
  margin-top: 10px;
  padding: 10px;
  background: #f9f9f9;
  border-radius: 6px;
}
.not-found {
  padding: 20px;
  color: red;
}
</style>
