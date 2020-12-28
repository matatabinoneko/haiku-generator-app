<template>
  <div class="container">
    <div>
      <b-form>
        <b-form-group
          id="input-group-keyword1"
          label="keyword1"
          label-for="input-keyword1"
          description="キーワードを入力して下さい"
        >
          <b-form-input
            id="input-keyword1"
            v-model="keyword1"
            placeholder="keyword1"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-keyword2"
          label="keyword2"
          label-for="input-keyword2"
          description="キーワードを入力して下さい"
        >
          <b-form-input
            id="input-keyword2"
            v-model="keyword2"
            placeholder="keyword2"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-keyword3"
          label="keyword3"
          label-for="input-keyword3"
          description="キーワードを入力して下さい"
        >
          <b-form-input
            id="input-keyword3"
            v-model="keyword3"
            placeholder="keyword3"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-prefix"
          label="prefix"
          label-for="input-prefix"
          description="上の句を入力して下さい"
        >
          <b-form-input
            id="input-prefix"
            v-model="prefix"
            placeholder="prefix"
            required
          ></b-form-input>
        </b-form-group>

        <b-button type="button" variant="primary" @click="get_haiku"
          >Submit</b-button
        >
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </div>
    <div><display-haiku haiku="haiku" /></div>
  </div>
</template>

<script>
import { DisplayHaiku } from '~/components/DisplayHaiku'
export default {
  components: {
    DisplayHaiku,
  },
  data: () => {
    return {
      keyword1: '',
      keyword2: '',
      keyword3: '',
      prefix: '',
    }
  },
  methods: {
    get_haiku() {
      const params = {
        key1: this.keyword1,
        key2: this.keyword2,
        key3: this.keyword3,
        prefix: this.prefix,
      }
      this.$axios.get(`/api/get_haiku`, { params }).then((res) => {
        console.log(res.data)
      })
    },
  },
}
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
