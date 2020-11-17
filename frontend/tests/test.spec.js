import {mount} from "@vue/test-utils";
import { assert } from 'chai'
import UserLogin from "../src/components/UserLogin.vue";

describe('First test to have an example on UserLogin', () => {
  it('when UserLogin is mounted it has an input, a label, and a button, but not a p', async() => {
    const wrapper = mount(UserLogin)
    assert.strictEqual(wrapper.contains("input"), true)
    assert.strictEqual(wrapper.contains("button"), true)
    assert.strictEqual(wrapper.contains("label"), true)
    assert.strictEqual(wrapper.contains("p"), false)
  })
})