<template>
  <tr>
    <td>{{ data2.name }}</td>
    <td>{{ data2.tags }}</td>
    <td>{{ data2.created_at }}</td>
  </tr>
</template>

<script>
export default {
  props: ["data2"],
}
</script>