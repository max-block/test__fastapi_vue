<template>
  <div id="nav">
    <router-link to="/data1">Data1</router-link>
    |
    <router-link to="/data2">Data2</router-link>
  </div>
  <router-view/>
</template>


<style>
table, th, td {
  border: 1px solid black;
}
</style>