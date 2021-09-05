<template>
  <v-row align="center" justify="center">
    <v-col cols="7">
      <Cropper
        ref="cropper"
        :src="img"
        :stencil-props="{
          handlers: {},
          movable: false,
          scalable: false
        }"
        :stencil-size="{
          width: 280,
          height: 280
        }"
        image-restriction="stencil"
        :debounce="true"
        :stencil-component="$options.components.CircleStencil"
      />
    </v-col>

    <v-col>
      <v-btn color="primary" @click="crop">
        crop
      </v-btn>
        <!-- <Preview
          :width="120"
          :height="120"
          :image="result.image"
          :coordinates="result.coordinates"
        /> -->
    </v-col>
  </v-row>
</template>

<script lang="ts">
  import { defineComponent, ref } from "@nuxtjs/composition-api";
  import { Cropper, CircleStencil, Preview } from 'vue-advanced-cropper';
  import 'vue-advanced-cropper/dist/style.css';

  export default defineComponent({
    name: 'ImageCrop',
    components: {
      Cropper,
      CircleStencil,
      Preview
    },

    setup (props, context) {
      const img = require('@/static/profile.jpg')
      const result = ref({
        coordinates: null,
        image: null
      })

      const crop = () => {
        console.log(context.refs);
        const { coordinates, image } = context.refs.cropper.getResult()
        result.value = { coordinates, image };
      }

      return {
        img,
        crop,
        result
      }
    }
  });
</script>

<style scoped>

</style>
