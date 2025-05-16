<template>
    <nav>
        <p>메인 페이지</p>
        <RouterLink :to="{ name: 'LandingView' }">
        </RouterLink>
    </nav>
    
    <RouterView />
</template>

<script setup>

</script>

<style scoped>

</style>