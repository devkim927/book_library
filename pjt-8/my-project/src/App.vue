<template>
    <nav>
        <RouterLink :to="{ name: 'LandingView' }"><p>Thread</p>
        </RouterLink>
        <RouterLink :to="{ name: 'BooksListView' }"><p>도서 목록</p>
        </RouterLink>
        <RouterLink :to="{ name: 'ThreadsListView' }"><p>쓰래드</p>
        </RouterLink>
    </nav>
    
    <RouterView />
</template>

<script setup>

</script>

<style scoped>

</style>