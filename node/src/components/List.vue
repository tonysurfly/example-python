<template>
  <ul>
    <li v-for="item in items">
      {{ item }}
      <span>{{ item }}</span>
    </li>
  </ul>
</template>

<script>
export default {
  name: 'list',
  props: [
    'items'
  ]
}
</script>
