<template>
  <div>
    <h1>Data2</h1>
    <data2-table :items="items"></data2-table>

  </div>
</template>

<script>
import Data2Table from "../components/Data2Table"
import axios from "axios"

export default {
  data() {
    return {
      items: [],
    }
  },
  components: {
    Data2Table
  },

  async created() {
    const res = await axios.get("http://localhost:3000/api/data2")
    this.items = res.data
  }

}
</script>