import time
import sys

from etl.controller.pipeline import PipelineExecutor

start = time.time()


def main(params: str = "USD-BRL"):
    new_exec = PipelineExecutor(params)
    new_exec.pipeline_run()


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) > 1:
        parameters = str(sys.argv[1])
        main(parameters)
    else:
        main()

print("Elapsed Time: ", round(time.time() - start, 2), "seconds")
