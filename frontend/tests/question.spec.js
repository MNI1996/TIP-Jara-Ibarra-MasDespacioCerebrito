import Vuex from 'vuex'
import {createLocalVue, mount} from "@vue/test-utils";
import {assert, expect} from 'chai'
import Question from "../src/components/Question.vue";

const localVue = createLocalVue()
localVue.use(Vuex)

describe('Question component test', () => {
    describe('with a store', () => {
        let store
        let getters
        let question = {
            "_id": {"$oid": "5fa608987e47352e90f0c8de"},
            "categories": ["Quimica"],
            "difficulty": 2,
            "options": [{
                "_id": {"$oid": "5fa608987e47352e90f0c8dc"},
                "correct": false,
                "sentence": "no-Cation"
            }, {
                "_id": {"$oid": "5fa608987e47352e90f0c8db"},
                "correct": true,
                "sentence": "Anion"
            }, {"_id": {"$oid": "5fa608987e47352e90f0c8dd"}, "correct": false, "sentence": "Negacation"}],
            "text": "Si el cation es un atomo con carga positiva, como se llama su contrario? "
        }

        beforeEach(() => {
            getters = {
                currentRoom: () => JSON.stringify({
                    "_id": "asdasd",
                    "categories": ["Quimica", "Fisica"],
                    "owner": "Ivan11",
                    "participants": ["Ivan11"],
                    "round_time": 60,
                    "rounds": [{
                        "_id": {"$oid": "5fc12fd84b1868a2750adde1"},
                        "answers": [],
                        "question": {"$oid": "5fa608987e47352e90f0c8de"}
                    }, {
                        "_id": {"$oid": "5fc12fd84b1868a2750adde2"},
                        "answers": [],
                        "question": {"$oid": "5fa6089f7e47352e90f0c8e2"}
                    }, {
                        "_id": {"$oid": "5fc12fd84b1868a2750adde3"},
                        "answers": [],
                        "question": {"$oid": "5fa608a67e47352e90f0c8e6"}
                    }, {
                        "_id": {"$oid": "5fc12fd84b1868a2750adde4"},
                        "answers": [],
                        "question": {"$oid": "5fa608ad7e47352e90f0c8ea"}
                    }, {
                        "_id": {"$oid": "5fc12fd84b1868a2750adde5"},
                        "answers": [],
                        "question": {"$oid": "5fa608d07e47352e90f0c8fe"}
                    }],
                    "rounds_amount": 5
                })
            }
            store = new Vuex.Store({getters})
        })
        it('when the user clicks on a option there is a selected option', () => {
            const wrapper = mount(Question, {
                store,
                localVue,
                propsData: { question }
            })
            expect(wrapper.find("#button-5fa608987e47352e90f0c8dd").exists()).to.be.true
            const optionButton = wrapper.find('#button-5fa608987e47352e90f0c8dd')
            assert.strictEqual(wrapper.vm.$data.selected, null);
            optionButton.trigger('click')
            assert.strictEqual(wrapper.vm.$data.selected !== null, true);
            assert.strictEqual(wrapper.vm.$data.selected._id.$oid, '5fa608987e47352e90f0c8dd');
        })
        it('if the user has not select an option the send answer button is disabled', () => {
            const wrapper = mount(Question, {
                store,
                localVue,
                propsData: { question }
            })
            expect(wrapper.find("#btn-enviar-respuesta").exists()).to.be.true
            const sendAnswerButton = wrapper.find('#btn-enviar-respuesta')
            assert.strictEqual(wrapper.vm.$data.selected, null);
            expect(sendAnswerButton.element.disabled).to.be.true
        })
        it('when the user selects an option the send answer button is not disabled', async() => {
            const wrapper = mount(Question, {
                store,
                localVue,
                propsData: { question }
            })
            expect(wrapper.find("#button-5fa608987e47352e90f0c8dd").exists()).to.be.true
            const optionButton = wrapper.find('#button-5fa608987e47352e90f0c8dd')
            await optionButton.trigger('click')

            expect(wrapper.find("#btn-enviar-respuesta").exists()).to.be.true
            const sendAnswerButton = wrapper.find('#btn-enviar-respuesta')
            expect(sendAnswerButton.element.disabled).to.be.false
        })
        it('when the user selects an option and send the answer the options buttons are disabled and the send answer button too', async() => {
            const wrapper = mount(Question, {
                store,
                localVue,
                propsData: { question },
                methods: {
                    async answerQuestion(){
                      this.answered = true;
                    },
                }
            })
            expect(wrapper.find("#button-5fa608987e47352e90f0c8dd").exists()).to.be.true
            const optionButton = wrapper.find('#button-5fa608987e47352e90f0c8dd')
            expect(optionButton.element.disabled).to.be.false
            await optionButton.trigger('click')

            expect(wrapper.find("#btn-enviar-respuesta").exists()).to.be.true
            const sendAnswerButton = wrapper.find('#btn-enviar-respuesta')
            expect(sendAnswerButton.element.disabled).to.be.false

            await sendAnswerButton.trigger('click')
            assert.strictEqual(wrapper.vm.$data.answered, true);
            expect(optionButton.element.disabled).to.be.true
            expect(sendAnswerButton.element.disabled).to.be.true
        })
    })
})