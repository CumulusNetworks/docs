class Air {
  constructor() {
    this.air_url = 'https://staging.air.nvidia.com';
    this.api_url = `${this.air_url}/api/v1`;
  }

  async _get(uri) {
    const res = await fetch(`${this.api_url}${uri}`, { method: 'GET', credentials: 'include' });
    return res.json();
  };

  async _post(uri) {
    const res = await fetch(`${this.api_url}${uri}`, { method: 'POST', credentials: 'include' });
    return res.json();
  };

  async autoprovision(sim) {
    let id;
    try {
      const res = await this._post(`/simulation/autoprovision/?simulation_id=${sim.refId}`);
      id = res['simulation']['id'];
    } catch (err) {
      console.error(err);
    }
    return id;
  };
}

class Simulation {
  constructor(refId) {
    this.refId = refId;
    this.id = undefined;
    this.air = new Air();
    this.initLoadingContainers();
  };

  initLoadingContainers() {
    document.querySelectorAll('[name*="loading-container"]').forEach(container => {
      container.setAttribute('src', `${this.air.air_url}/loading?message=Building%20Simulation`);
    });
  }

  async loadConsoles() {
    const loadingContainers = document.getElementsByName(`loading-container-${this.refId}`);
    const containers = document.getElementsByName(`console-container-${this.refId}`);
    containers.forEach((container, idx) => {
      container.addEventListener('load', () => {
        setTimeout(() => {
          container.classList.remove('terminal-hidden');
          if (loadingContainers[idx]) {
            loadingContainers[idx].classList.add('terminal-hidden');
          }
        }, 1000); // small delay to avoid flicker when switching between iframes
      });
      container.setAttribute('src', `${this.air.air_url}/Terminal?simulation_id=${this.id}`);
    });
  };

  initHandler(el) {
    const self = this;
    el.addEventListener('click', async () => {
      if (!this.id) {
        self.id = await self.air.autoprovision(self);
        self.loadConsoles();
      }
    });
  };
}
