<template>
  <tr>
    <td>{{ data1.name }}</td>
    <td>{{ data1.value }}</td>
    <td>{{ data1.created_at }}</td>
  </tr>
</template>

<script>
export default {
  props: ["data1"],
}
</script>