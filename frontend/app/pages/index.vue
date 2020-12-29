<template>
  <div class="container">
    <Introduction class="mt-5" />
    <div class="row">
      <div class="col col-sm-12 px-0">
        <b-form>
          <b-card bg-variant="light">
            <b-form-group
              class="mb-0"
              description="ローマ字や数字，記号は入力できません"
            >
              <b-form-group
                label="キーワード:"
                label-cols-sm="3"
                label-align-sm="right"
              >
                <b-form-input
                  id="keyword1"
                  v-model="keyword1"
                  required
                ></b-form-input>
              </b-form-group>

              <b-form-group
                label="キーワード:"
                label-cols-sm="3"
                label-align-sm="right"
              >
                <b-form-input
                  id="keyword2"
                  v-model="keyword2"
                  required
                ></b-form-input>
              </b-form-group>

              <b-form-group
                label="キーワード:"
                label-cols-sm="3"
                label-align-sm="right"
              >
                <b-form-input
                  id="keyword3"
                  v-model="keyword3"
                  required
                ></b-form-input>
              </b-form-group>

              <b-form-group
                label="上の句:"
                label-cols-sm="3"
                label-align-sm="right"
              >
                <b-form-input
                  id="prefix"
                  v-model="prefix"
                  required
                ></b-form-input>
              </b-form-group>
            </b-form-group>

            <b-alert :show="errorMessage !== null" variant="warning">{{
              errorMessage
            }}</b-alert>
            <div class="float-right">
              <b-button
                type="button"
                variant="success"
                :disabled="isRequest"
                @click="get_haiku"
                >ここで一句</b-button
              >
              <b-button type="reset" variant="danger">リセット</b-button>
            </div>
          </b-card>
        </b-form>
      </div>
    </div>
    <div class="row justify-content-center my-5">
      <div class="col-sm-6 d-flex justify-content-center">
        <display-haiku v-if="showHaiku" :haiku="haiku" />
      </div>
    </div>
  </div>
</template>

<script>
import DisplayHaiku from '~/components/DisplayHaiku'
import Introduction from '~/components/Introduction'
export default {
  components: {
    DisplayHaiku,
    Introduction,
  },
  data: () => {
    return {
      keyword1: '',
      keyword2: '',
      keyword3: '',
      prefix: '',
      haiku: null,
      errorMessage: null,
      isRequest: false,
      showHaiku: false,
    }
  },
  methods: {
    get_haiku() {
      // ボタン連打を回避
      this.isRequest = true

      // keywordとprefixが日本語かを確認
      if (
        !(
          this.isJapaneseWord(this.keyword1) &&
          this.isJapaneseWord(this.keyword2) &&
          this.isJapaneseWord(this.keyword3) &&
          this.isJapaneseWord(this.prefix)
        )
      ) {
        this.errorMessage = '日本語を入力してください'
        this.isRequest = false
        return
      }

      // prefixが5文字以内かを確認
      if (!this.isValidLength(this.prefix)) {
        this.errorMessage = '上の句は5文字以内にして下さい'
        this.isRequest = false
        return
      }

      this.errorMessage = null
      this.haiku = ''
      this.showHaiku = true

      const params = {
        key1: this.keyword1,
        key2: this.keyword2,
        key3: this.keyword3,
        prefix: this.prefix,
      }
      this.$axios
        .get('/get_haiku', { params })
        .then((res) => {
          this.haiku = res.data.haiku
          this.isRequest = false
        })
        .catch(() => {
          this.errorMessage = 'エラーが発生しました'
          this.showHaiku = false
          this.isRequest = false
        })
    },
    isJapaneseWord(str) {
      // 日本語であるかを判定
      if (
        str === '' ||
        str.match(/^[\u30A0-\u30FF\u3040-\u309F\u3005-\u3006\u30E0-\u9FCF]+$/)
      ) {
        return true
      } else {
        return false
      }
    },

    isValidLength(str) {
      // 日本語で5文字以内か検証
      if (str.length <= 5) {
        return true
      } else {
        return false
      }
    },
  },
}
</script>
