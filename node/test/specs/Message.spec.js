import { shallowMount } from '@vue/test-utils'
import Message from '@/components/Message'

describe('Message', () => {
  it('renders props.msg when passed', () => {
    const msg = 'new message'
    const wrapper = shallowMount(Message, {
      context: { props: { msg } }
    })
    expect(wrapper.text()).toBe(msg)
  })
})
