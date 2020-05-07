<template>
  <div class="fluid-container">
    <div class="wrapper">
      <div
        v-for="(data, i) in json"
        :key="i"
        class="card"
        :class="{active: selected.includes(i), disabled: !data['Download URL']}"
        @click="select(i)"
      >
        <img
          class="card-img-top"
          :src="`${publicPath}images/${data['Book Title']}_${data['Copyright Year']}.jpg`"
          alt="Missing Textbook Image"
        />
        <div class="card-body">
          <h5 class="card-title">{{data['Book Title']}}</h5>
        </div>
      </div>
    </div>
    <button
      type="button"
      class="download btn btn-primary"
      :class="{disabled: !selected.length}"
      @click="downloadItems()"
    >Download</button>
  </div>
</template>

<script>
import json from "../json/Free+English+textbooks+with+download_url.json";
import axios from "axios";

const apiEndpoint = "http://127.0.0.1:5000/"

export default {
  name: "HelloWorld",
  data() {
    return {
      publicPath: process.env.BASE_URL,
      json: json,
      selected: []
    };
  },
  methods: {
    select(i) {
      this.selected.includes(i)
        ? this.selected.splice(this.selected.indexOf(i), 1)
        : this.selected.push(i);
    },
    downloadItems() {
      let data_list = [];
      for (let i = 0; i < this.selected.length; i++) {
        const data = this.json[this.selected[i]];
        const downloadUrl = data["Download URL"];
        const label = data["Book Title"] + ' ' + data["Edition"] + ', ' + data["Copyright Year"];
        data_list.push({ downloadUrl, label });
      }
      const json = {...data_list}
      axios({
        method: "post",
        url: apiEndpoint,
        data: json
      })
        .then(response => console.log("<3"))
        .catch(err => console.log(`Error: ${err}`));
    }
  }
};
</script>

<style scoped>
.card.disabled {
  pointer-events: none;
  opacity: 0.3;
}
.btn.disabled {
  cursor: default;
}
.fluid-container {
  display: flex;
  justify-content: center;
}
.card:hover {
  cursor: pointer;
  box-shadow: 0 0 60px 0 rgba(0, 0, 0, 0.25);
}
.card.active {
  cursor: pointer;
  box-shadow: 0 0 20px 0 rgb(0, 0, 0);
}
.card {
  margin-bottom: 50px;
  width: 15%;
}
.card-body {
  display: flex;
  align-items: center;
  justify-content: center;
}
.card-title {
  margin-bottom: 0;
  font-size: var(--default-font-size);
}
.wrapper {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  position: relative;
  padding: 20px;
  max-width: 1400px;
}
.download {
  position: fixed;
  height: 50px;
  bottom: 40px;
  width: 100%;
  max-width: 200px;
}
@media only screen and (max-width: 992px) {
  .card {
    width: 22%;
  }
}
@media only screen and (max-width: 768px) {
  .card {
    width: 45%;
  }
}
@media only screen and (max-width: 600px) {
  .card {
    width: 100%;
  }
}
</style>
