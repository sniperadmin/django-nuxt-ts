<template>
  <v-form
    ref="formRef"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="name"
      :counter="10"
      :rules="nameRules"
      label="Name"
      required
    ></v-text-field>

    <!-- <v-text-field
      v-model="email"
      :rules="emailRules"
      label="E-mail"
      required
    ></v-text-field> -->

    <v-text-field
      v-model="password"
      :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
      :rules="passwordRules"
      :type="show ? 'text' : 'password'"
      name="input-10-1"
      label="Normal with hint text"
      hint="At least 8 characters"
      counter
      @click:append="show = !show"
    ></v-text-field>

    <v-checkbox
      v-model="checkbox"
      :rules="[v => !!v || 'You must agree to continue!']"
      label="Do you agree?"
      required
    ></v-checkbox>

    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="validate"
    >
      Validate
    </v-btn>
  </v-form>
</template>

<script lang="ts">
import { defineComponent, ref, reactive, useContext } from '@nuxtjs/composition-api'

export default defineComponent({
  setup (props, context) {
    const valid = ref(true)
    // const formRef = ref(null)
    const name = ref('nashuser')
    const email = ref('')
    const password = ref('nash123456')
    const checkbox = ref(false)
    const show = ref(false)

    const { $auth, $axios } = useContext()

    const nameRules = reactive([
      (v: [boolean, string]) => !!v || 'Name is required!',
      (v: [boolean, string]) => (v && v.length <= 10) || 'Name must be less than 10 characters'
    ])

    const emailRules = reactive([
      (v: [boolean, string]) => !!v || 'E-mail is required!',
      (v: any) => /.+@.+\..+/.test(v) || 'Name must be less than 10 characters'
    ])

    const passwordRules = reactive([
      (v: [boolean, string]) => !!v || 'password is required!',
      (v: any) => v.length >= 6 || 'Min 6 characters'
    ])

    const isLoggedIn = $auth.loggedIn

    const validate = async function() {
      if (context.refs.formRef.validate()) {
        try {
          const { data } = await $auth.loginWith('local', {
            data: {
              username: name.value,
              password: password.value
            }
          })

        } catch (error) {
          console.log(error);
        }
      }
    }

    return {
      valid,
      name,
      email,
      nameRules,
      emailRules,
      password,
      checkbox,
      show,
      passwordRules,
      validate,
      isLoggedIn,
    }
  }
})
</script>

<style scoped>

</style>
