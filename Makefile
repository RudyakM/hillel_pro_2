check:
	black --check ./ && flake8 ./ && isort --check-only ./

fix:
	black ./ && flake8 ./ && isort ./