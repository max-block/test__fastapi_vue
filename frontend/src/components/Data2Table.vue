<template>
  <table>
    <tr>
      <th>name</th>
      <th>tags</th>
      <th>created_at</th>
    </tr>
    <data2-row v-for="d in items" :key="d.id" :data2="d"></data2-row>
  </table>
</template>

<script>
import Data2Row from "./Data2Row"

export default {
  props: ["items"],
  components: {
    Data2Row
  }
}
</script>