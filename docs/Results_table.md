| Experiment | Initiator | Failed Node | Expected Alive Nodes | Expected Outcome | Actual Propagation Time | Status |
|------------|-----------|-------------|----------------------|------------------|-------------------------|--------|
| E1 | A | B | A, C | Message reaches A and C only | 0.0066 seconds, 0.0037 , - 0.0081 seconds| Verified (A & C received, B ignored) |
| E2 | A | None | A, B, C | All nodes receive message | 0.0083 seconds. 0.0060 seconds. 0.0047 seconds. | Verified (A, B, C received) |
| E3 | C | B | A, C | Message reaches A and C only | 0.0071 seconds.0.0052 seconds. 0.0041 seconds.|Verified (C, A received, B ignored) |
| E4 | B | None | A, B, C | All nodes receive message | 0.007804099997883895. 0.0046 seconds. 0.0110 seconds.| ( B, C, A received).|