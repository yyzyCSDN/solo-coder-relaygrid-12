from relaygrid.analysis.scenarios import pareto_front
from relaygrid.planning.reconductoring import rank_projects
from relaygrid.reliability.montecarlo import simulate_failures


def test_planning_results_are_unique_and_independent_of_input_order():
    rates_ab = {"A": 0.2, "B": 0.8}
    rates_ba = {"B": 0.8, "A": 0.2}
    assert simulate_failures(rates_ab, 1.0, seed=0) == simulate_failures(rates_ba, 1.0, seed=0)

    cases = [
        {"id": "P1", "benefit": 10.0, "cost": 5.0},
        {"id": "P1", "benefit": 10.0, "cost": 5.0},
        {"id": "P2", "benefit": 9.0, "cost": 6.0},
    ]
    assert pareto_front(cases, "benefit", "cost") == [cases[0]]

    ranked = rank_projects(
        [("A", 100.0, 1.0, 0.0), ("B", 100.0, 1.0, 0.0)]
    )
    assert ranked == [(10.0, "A"), (10.0, "B")]
