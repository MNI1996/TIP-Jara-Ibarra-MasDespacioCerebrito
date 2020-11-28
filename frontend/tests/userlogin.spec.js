import {createLocalVue, mount} from "@vue/test-utils";
import chai, {assert, expect} from 'chai'
import sinon from "sinon";
import sinonChai from "sinon-chai";
import UserLogin from "../src/components/UserLogin.vue";

chai.use(sinonChai);

const localVue = createLocalVue()

describe('UserLogin component test', () => {

    const mockMethod = sinon.spy();

    it('if the nick is not 3 characters length, the login button is disabled', async () => {
        const wrapper = mount(UserLogin, {
            localVue,
        })
        await wrapper.setData({password: '123456'})
        expect(wrapper.find("#nick").exists()).to.be.true
        const nickInput = wrapper.find('#nick')
        await nickInput.setValue("as")
        assert.strictEqual(nickInput.element.value, "as");
        const loginButton = wrapper.find('button')
        expect(loginButton.element.disabled).to.be.true
    })
    it('if the nick is 3 characters length, the login button is not disabled', async () => {
        const wrapper = mount(UserLogin, {
            localVue,
        })
        await wrapper.setData({password: '123456'})
        expect(wrapper.find("#nick").exists()).to.be.true
        const nickInput = wrapper.find('#nick')
        await nickInput.setValue("asd")
        assert.strictEqual(nickInput.element.value, "asd");
        const loginButton = wrapper.find('button')
        expect(loginButton.element.disabled).to.be.false
    })
    it('if the nick is 5 characters length, the login button is not disabled', async () => {
        const wrapper = mount(UserLogin, {
            localVue,
        })
        await wrapper.setData({password: '123456'})
        expect(wrapper.find("#nick").exists()).to.be.true
        const nickInput = wrapper.find('#nick')
        await nickInput.setValue("asdf")
        assert.strictEqual(nickInput.element.value, "asdf");
        const loginButton = wrapper.find('button')
        expect(loginButton.element.disabled).to.be.false
    })
    it('if the password is less than 6 characters length, the login button is disabled', async () => {
        const wrapper = mount(UserLogin, {
            localVue,
        })
        await wrapper.setData({nick: '123456'})
        expect(wrapper.find("#pass").exists()).to.be.true
        const passwordInput = wrapper.find('#pass')
        await passwordInput.setValue("asdf")
        assert.strictEqual(passwordInput.element.value, "asdf");
        const loginButton = wrapper.find('button')
        expect(loginButton.element.disabled).to.be.true
    })
    it('if the password is  6 characters length, the login button is not disabled', async () => {
        const wrapper = mount(UserLogin, {
            localVue,
        })
        await wrapper.setData({nick: '123456'})
        expect(wrapper.find("#pass").exists()).to.be.true
        const passwordInput = wrapper.find('#pass')
        await passwordInput.setValue("654321")
        assert.strictEqual(passwordInput.element.value, "654321");
        const loginButton = wrapper.find('button')
        expect(loginButton.element.disabled).to.be.false
    })
    it('if the user set correct values the button can be clicked and login method is triggered', async () => {
        const wrapper = mount(UserLogin, {
            localVue,
        })
        wrapper.setMethods({login: mockMethod});
        await wrapper.setData({nick: '123456'})
        await wrapper.setData({password: '123456'})

        const loginButton = wrapper.find('button')
        expect(loginButton.element.disabled).to.be.false
        await loginButton.trigger('click')
        expect(mockMethod).to.have.been.called
    })
})