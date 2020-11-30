<template>
  <div>
    <h1>Data1</h1>
    <data1-table :items="items"></data1-table>

  </div>
</template>

<script>
import Data1Table from "../components/Data1Table"
import axios from "axios"

export default {
  data() {
    return {
      items: [],
    }
  },
  components: {
    Data1Table
  },

  async created() {
    const res = await axios.get("http://localhost:3000/api/data1")
    this.items = res.data
  }

}
</script>