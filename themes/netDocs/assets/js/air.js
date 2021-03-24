class Air {
  constructor() {
    this.api_url = 'https://staging.air.nvidia.com/api/v1';
  }

  autoprovision(sim) {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `${this.api_url}/simulation/autoprovision/?simulation_id=${sim.id}`, true);
    xhr.send();
  }
}

class Simulation {
  constructor(id) {
    this.id = id;
  }

  initHandler(el) {
    el.addEventListener('click', () => {
      const air = new Air()
      air.autoprovision(this);
    });
  }
}
