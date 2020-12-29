<template>
  <section class="haiku haiku-font">
    <div class="haiku-inner">
      <div class="haiku-ku">
        <p v-if="haiku">{{ haiku }}</p>
        <div v-else>
          <div>
            <b-spinner
              class="d-inline-block"
              variant="success"
              type="grow"
              label="Spinning"
            ></b-spinner>
            <p class="d-inline-block">作成中</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  props: {
    haiku: {
      type: String,
      required: true,
    },
    // showHaiku: {
    //   type: Boolean,
    //   required: true,
    // },
  },
}
</script>

<style scoped>
.haiku {
  writing-mode: vertical-rl; /* CSS3 (Firefox, Edge) */
  -webkit-writing-mode: vertical-rl; /* Chrome, Opera, Safari */
  -ms-writing-mode: tb-rl;
}
.haiku p {
  margin: 0;
  padding: 0;
}
.haiku-inner {
  /* position: relative;
  top: 0;
  right: 50%; */
  padding: 6px;
  display: block;
  transform: translate(50%, 0%);
  background-image: linear-gradient(
    to top left,
    #f7de06,
    #e0a020,
    #edac06,
    #f7de06,
    #ecb802,
    #ebbf10,
    #d0a000
  );
  box-shadow: 2px 2px 8px 4px rgba(0, 0, 0, 0.1);
}
.haiku-ku {
  padding: 30px 50px 40px 50px;
  font-size: 2.5rem;
  line-height: 3rem;
  white-space: nowrap;
  background-color: #fafaf6;
}
</style>
