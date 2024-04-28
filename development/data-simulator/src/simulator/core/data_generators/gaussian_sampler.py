import logging
import random

from simulator.core.data_generators.abstract_sampler import (
    AbstractSampler,
    AbstractSamplerParams,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GaussianSamplerParams(AbstractSamplerParams):
    mean: float = 0.1
    variance: float = 1.0


class GaussianSampler(AbstractSampler):
    def __init__(self, params: GaussianSamplerParams | None = None):
        super().__init__(params)
        self.params = params or GaussianSamplerParams()

    def sample_one(self) -> float:
        sampled_value = random.gauss(self.params.mean, self.params.variance**0.5)
        logger.debug(f"Sampled value: {sampled_value}")
        return sampled_value
