<template>
  <table>
    <tr>
      <th>name</th>
      <th>value</th>
      <th>created_at</th>
    </tr>
    <data1-row v-for="d in items" :key="d.id" :data1="d"></data1-row>
  </table>
</template>

<script>
import Data1Row from "./Data1Row"

export default {
  props: ["items"],
  components: {
    Data1Row
  }
}
</script>
