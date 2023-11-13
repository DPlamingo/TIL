import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', () => {
  const balances = ref([
    {
      name: '김하나',
      balance: 100000
      },
      {
      name: '김두리',
      balance: 10000
      },
      {
      name: '김서이',
      balance: 100
      },
    ])

  const getUserInfo = computed(() => {
    return (name) => {
      return balances.value.find(info => {
        return info.name === name
      })
    } // 그 값은 어떻게 만드겠냐? 인자를 넘겨줬다 가정하고 씀
    // 그 값을 콜백 펑션에다가 컴퓨티드 이친구 겟으로 불러옴
    // 넘겨받은 이 name 값을 다시 에로우 펑션으로 다시 처리
  })
  const updateBalance = function (name) {
    const info = balances.value.find(info => {
      return info.name === name
    })
    info.balance += 1000
  }
  return { 
    balances, getUserInfo, updateBalance 
  }
})
