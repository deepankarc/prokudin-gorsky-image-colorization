import get_similarity as gsim

# align the channels
def align_image_channels_pyramids(img, row_idx, col_idx, DELTA, SIM_INDEX = 'SSD'):
  ch_ref = img[0,:,:] # reference channel
  rshift = np.zeros(2,dtype=np.int32) # shifts for optimal alignment
  cshift = np.zeros(2,dtype=np.int32)
  
  for ch in range(1,3):
    if(SIM_INDEX == 'SSD'):
      best_sim_score = float('inf')
      ineq_expr = 'sim_score < best_sim_score'
    else:
      best_sim_score = float('-inf')
      ineq_expr = 'sim_score > best_sim_score'
  
    # shift for each plausible row and column
    for u in range(row_idx[ch-1]-DELTA, row_idx[ch-1]+DELTA+1):
      for v in range(col_idx[ch-1]-DELTA, col_idx[ch-1]+DELTA+1):
        # best alignment for channels
        ch_dis = np.roll(img[ch,:,:], (u,v), axis=(0,1))
        sim_score = gsim.get_similarity(ch_ref, ch_dis, SIM_INDEX)
        if(eval(ineq_expr)):
          best_sim_score = sim_score
          rshift[ch-1] = u
          cshift[ch-1] = v
  
  return [rshift, cshift]
