<template>
  <div v-if="loading">로딩 중...</div>
  <div v-else-if="thread">
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

const route = useRoute()
const threadId = parseInt(route.params.threadId)

const thread = ref(null)
const loading = ref(true)

onMounted(async () => {
  try {
    const stored = localStorage.getItem('threads')
    const parsed = stored ? JSON.parse(stored) : []
    const found = parsed.find(t => t.id === threadId)

    await new Promise(resolve => setTimeout(resolve, 300))
    thread.value = found
  } catch (err) {
    console.error('스레드 로드 중 오류:', err)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.thread-content {
  background: #f9f9f9;
  padding: 10px;
}
</style>