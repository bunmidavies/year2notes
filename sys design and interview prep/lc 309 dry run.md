prices = [1,2,3,0,2]

we have 3 possible states:
- holding a stock
  possible moves from here are **sell**, or **rest**
- sold a stock
  only possible move from here is **rest**
- resting with no stock
  possible moves from here are **buy**, and **rest**

we say that:
- s0 = resting with no stock
- s1 = holding stock
- s2 = just sold stock

therefore

- index 0 - set initial vals
s0[0] = 0
s1[0] = -prices[0] = -1
s2[0] = Integer.MIN_VALUE

- index 1 - prices[1] = 2
s0[1] = max(0,Integer.MIN_VALUE) = 0
s1[1] = max(-1, -2) = -1
s2[1] = -1 + 2 = 1

- index 2 - prices[2] = 3
s0[2] = max(0,1) = 1
s1[2] = max(-1,1 - 3) = -1
s2[2] = -1 + 3 = 2

- index 3 - prices[3] = 0
s0[3] = max(1,2) = 2
s1[3] = max(-1,1-0) = 1
s2[3] = -1 + 0 = -1

- index 4 - prices[4] = 2
s0[4] = max(2,-1) = 2
s1[4] = max(1,2-2) = 1
s2[4] = 1 + 2 = 3

result is max(s0[4],s2[4]) which = 3

what if prices = [1,2,300,0,2] ?

- index 0 - set initial vals
s0[0] = 0
s1[0] = -prices[0] = -1
s2[0] = Integer.MIN_VALUE

- index 1 - prices[1] = 2
s0[1] = max(0,Integer.MIN_VALUE) = 0
s1[1] = max(-1, -2) = -1
s2[1] = -1 + 2 = 1

- index 2 - prices[2] = 300
s0[2] = max(0,1) = 1
s1[2] = max(-1,1 - 300) = -299
s2[2] = -1 + 300 = 299

- index 3 - prices[3] = 0
s0[3] = max(1,299) = 299
s1[3] = max(-299,1-0) = 1
s2[3] = -299 + 0 = -299

- index 4 - prices[4] = 2
s0[4] = max(299,-299) = 299
s1[4] = max(1,299-2) = 297
s2[4] = 1 + 2
