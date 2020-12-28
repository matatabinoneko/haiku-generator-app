<template>
  <p>{{ haiku }}</p>
</template>

<script>
export default {
  props: {
    haiku: {
      type: String,
      required: true,
    },
  },
}
</script>
