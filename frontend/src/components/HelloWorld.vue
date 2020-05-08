<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h3>Data from the API</h3>
    <table>
      <thead>
        <tr>
          <th>id</th>
          <th>uuid</th>
          <th>slug</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="r in rows" :key="r.id">
          <td>{{ r.id }}</td>
          <td>{{ r.uuid }}</td>
          <td>{{ r.slug }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
const API_HOST = process.env.NODE_ENV === 'production' ? '' : 'http://localhost:5000'

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data () {
    return {
      rows: []
    }
  },
  mounted () {
    fetch(`${API_HOST}/api`).then(res => {
      return res.json()
    }).then(data => {
      this.rows = data
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
table {
  margin-right: auto;
  margin-left: auto;
}
</style>
