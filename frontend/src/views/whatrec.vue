<template>
  <div id="contents">
    <div id="left" class="column">
      <Searchbar />
    </div>
    <div id="right" class="column">
      <div v-for="match in record_info" :key="match.pv_name">
        <Recordinfo
          v-for="(whatrec, idx) in match.info"
          :key="idx"
          :whatrec="whatrec"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

import Recordinfo from "../components/recordinfo.vue";
import Searchbar from "../components/searchbar.vue";

export default {
  name: "WhatRec",
  components: {
    Recordinfo,
    Searchbar,
  },
  props: [],
  computed: {
    record_glob() {
      return this.$route.params.record_glob || "";
    },
    selected_records() {
      const records = this.$route.params.selected_records;
      return (records || "").split("|");
    },
    ...mapState({
      record_info(state) {
        let record_info = [];
        for (const rec of this.selected_records) {
          if (rec in state.record_info) {
            record_info.push(state.record_info[rec]);
          }
        }
        return record_info;
      },
    }),
  },
  data() {
    return {};
  },
  created() {
    console.debug(
      `whatrecord Mounted: glob=${this.record_glob} PVs=${this.selected_records}`
    );
  },
};
</script>

<style scoped>
#contents {
  flex-direction: row;
  justify-content: flex-start;
  display: flex;
  overflow: scroll;
  height: 93vh;
}

.column {
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  justify-content: flex-start;
  overflow: scroll;
}

#left {
  min-width: 15%;
  max-width: 20%;
  border-right: 1px dotted;
}

#right {
  margin: 1em;
  min-width: 75%;
  max-width: 100%;
}
</style>
