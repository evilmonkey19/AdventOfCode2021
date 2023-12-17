# x1, x2 = 20, 30
# y1, y2 = -10, -5

x1, x2 = 79, 137
y1, y2 = -176, -117

best_y = 0

# Movimiento Rectilíneo Uniforme (MRU)

for init_vx in range(1, x2 + 1): # Cannot go higher than x2
    for init_vy in range(y1, 500):
        vx, vy = init_vx, init_vy
        x, y, max_y = 0, 0, y1
        while x <= x2 and y >= y1:
            max_y = max(max_y, y)
            if x1 <= x <= x2 and y1 <= y <= y2:
                best_y = max(best_y, max_y)
                break
            x += vx
            y += vy
            vx = max(0, vx - 1)
            vy -= 1
 
print(best_y)


