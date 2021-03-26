class Air {
  constructor() {
    this.api_url = 'https://staging.air.nvidia.com/api/v1';
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

  async getNodes(sim) {
    return this._get(`/simulation-node/?simulation=${sim.id}`);
  }
}

class Simulation {
  constructor(refId) {
    this.refId = refId;
    this.id = undefined;
    this.air = new Air();
  }

  async loadConsoles() {
    const nodes = await this.air.getNodes(this);
    console.log(nodes);
  };

  initHandler(el) {
    const self = this;
    el.addEventListener('click', async () => {
      self.id = await self.air.autoprovision(self);
      self.loadConsoles();
    });
  };
}
