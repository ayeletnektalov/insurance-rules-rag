from graph.state import ConstructionState


def pricing_agent(state: ConstructionState):
    print("Pricing Agent Running")

    prices = state.get("prices", {})
    tasks = state.get("detected_tasks", {})

    wall_price = prices.get("wall_price", 500)
    kitchen_price = prices.get("kitchen_price", 3000)
    pipeline_price = prices.get("pipeline_price", 100)

    walls_cost = tasks.get("walls", 0) * wall_price
    kitchen_cost = tasks.get("kitchen", 0) * kitchen_price
    pipeline_cost = tasks.get("pipeline", 0) * pipeline_price

    state["cost_breakdown"] = {
        "walls_cost": walls_cost,
        "kitchen_cost": kitchen_cost,
        "pipeline_cost": pipeline_cost,
        "total_cost": walls_cost + kitchen_cost + pipeline_cost
    }

    return state