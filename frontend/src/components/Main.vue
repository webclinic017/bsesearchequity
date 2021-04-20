<template>
  <div>
    <Header/>
    <div class="search">

      <div class="pad-15-hor pad-15-ver search-parent">
        <div class="search-bar" >
          <b-form-input

              @click="searchdata"
            v-model="name"
            type="submit"
            placeholder="EQUITY  DATA SEARCH"
          ></b-form-input>
          <span class="search-icon">
            <i class="fas fa-search"></i>
          </span>

          <br>

          <div class="search_action">
            <button
                type="submit"
                class="search_btn btn btn-primary"
                @click="searchdata"
            >
            <span >
              Equity search
            </span>

            </button>
          </div>
        </div>


      </div>
    </div>
    <table class="results_table table table-striped" v-if="results && results.length > 0">
      <thead>
      <tr>

        <th scope="col" class="sc_name">
          <a
              role="button"
              data-mdb-toggle="tooltip"

          >INSTRUMENT NAME</a
          >
        </th>

        <th scope="col">
          <a
              role="button"
              data-mdb-toggle="tooltip"

          >open</a
          >
        </th>
        <th scope="col">
          <a
              role="button"
              data-mdb-toggle="tooltip"

          >high</a
          >
        </th>
        <th scope="col">
          <a
              role="button"
              data-mdb-toggle="tooltip"
          >low</a
          >
        </th>
        <th scope="col">
          <a
              role="button"
              data-mdb-toggle="tooltip"

          >close</a
          >
        </th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(result) in results" :key="result.keyname">

        <td class="sc_name">{{result.keyname}}</td>
        <td>{{result.open}}</td>
        <td>{{result.high}}</td>
        <td>{{result.low}}</td>
        <td>{{result.close}}</td>
      </tr>
      </tbody>
    </table>


  </div>
</template>


<script>
import Header from "@/components/Header.vue";
import axios from 'axios';
export default {
  name: 'searchbox',
  data() {
    return {
      name: null,
      results: [],
      notFound: false
    };
  },
  methods: {
    checkForm(e) {
      e.preventDefault();
    },
    searchdata() {
     //const api = "http://134.209.148.230:8000/api/input?name="
      const api = "http://0.0.0.0:8000/api/input?name="


      if (this.name && this.name.length) {
        // eslint-disable-next-line no-console
        console.log(this.name);
        const apiWithKeyUrl = api + this.name;

        this.results = [];
        axios
            .get(apiWithKeyUrl)
            .then(
                (response) => {

                  this.notFound = false;

                  this.results = response["data"]["outputfromdb"]
                }, err =>{

                  // eslint-disable-next-line no-console
                  console.log(err);
                });
      }
    },
  },

components: {
  Header
}
};
</script>



<style scoped  lang="scss">
  @import "../styles/main.scss";
</style>


