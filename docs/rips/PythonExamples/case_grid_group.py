import os
import rips

resinsight = rips.Instance.find()

case_paths = []
case_paths.append(
    "C:/Users/lindk/source/repos/ResInsight/TestModels/Case_with_10_timesteps/Real0/BRUGGE_0000.EGRID"
)
case_paths.append(
    "C:/Users/lindk/source/repos/ResInsight/TestModels/Case_with_10_timesteps/Real10/BRUGGE_0010.EGRID"
)
for case_path in case_paths:
    assert os.path.exists(
        case_path
    ), "You need to set valid case paths for this script to work"

case_group = resinsight.project.create_grid_case_group(case_paths=case_paths)

case_group.compute_statistics()

view = case_group.views()[0]
view.apply_cell_result("DYNAMIC_NATIVE", "PRESSURE_DEV")
