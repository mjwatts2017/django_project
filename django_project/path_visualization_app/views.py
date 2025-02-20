import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import heapq

def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    pq = [(0, start)]  # (distance, (x, y))
    distances = {start: 0}
    parents = {start: None}

    while pq:
        current_distance, (x, y) = heapq.heappop(pq)
        if (x, y) == end:
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:  # Assuming 0 is a walkable cell
                new_distance = current_distance + 1
                if (nx, ny) not in distances or new_distance < distances[(nx, ny)]:
                    distances[(nx, ny)] = new_distance
                    parents[(nx, ny)] = (x, y)
                    heapq.heappush(pq, (new_distance, (nx, ny)))

    path = []
    node = end
    while node:
        path.append(node)
        node = parents.get(node)
    path.reverse()
    
    return path

@csrf_exempt  # Temporarily allow CSRF-exempt for testing
def find_shortest_path(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            grid = data.get("grid")
            start = tuple(data.get("start"))
            end = tuple(data.get("end"))

            if not grid or not start or not end:
                return JsonResponse({"error": "Missing required data"}, status=400)

            # Call the pathfinding algorithm (replace with real logic)
            path = dijkstra(grid, start, end)
            return JsonResponse({"path": path})

        return JsonResponse({"error": "Please use a POST request."}, status=405)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def grid_view(request):
    return render(request, "index.html")