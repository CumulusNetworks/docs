class Air {
  constructor() {
    this.air_url = 'https://air.nvidia.com';
    this.api_url = `${this.air_url}/api/v1`;
  }

  async _request(method, uri, payload, options) {
    const res = await fetch(
      `${this.api_url}${uri}`, { ...options, body: payload, method, credentials: 'include' },
    );
    if (res.status > 399) {
      throw new Error(res.statusText);
    }
    return res;
  }

  async _get(uri) {
    const res = await this._request('GET', uri);
    return res.json();
  };

  async _post(uri, payload) {
    const res = await this._request(
      'POST', uri, JSON.stringify(payload), { headers: { 'Content-type': 'application/json' }},
    );
    return res.json();
  };

  async autoprovision(sim) {
    let id;
    try {
      const res = await this._post(
        `/simulation/autoprovision/?simulation=${sim.refName}`, { source: 'docs' },
      );
      id = res['simulation']['id'];
    } catch (err) {
      console.error(err);
    }
    return id;
  };
}

class Simulation {
  constructor(refName, autoLoad) {
    this.refName = refName;
    this.autoLoad = autoLoad;
    this.id = undefined;
    this.air = new Air();
    // this.initLoadingContainers(); // Only needed for legacy Air UI
  };

  initLoadingContainers() {
    document.querySelectorAll('[name*="loading-container"]').forEach(container => {
      container.setAttribute('src', `${this.air.air_url}/loading?message=Building%20Simulation`);
    });
  };

  async loadConsoles() {
    const loadingContainers = document.getElementsByName(`loading-container-${this.refName}`);
    const containers = document.getElementsByName(`console-container-${this.refName}`);
    let src = `${this.air.air_url}/terminal`;
    src += `?simulation_id=${this.id}&hideOOB=true&autoLoad=${this.autoLoad}`;
    containers.forEach((container, idx) => {
      container.addEventListener('load', () => {
        setTimeout(() => {
          container.classList.remove('terminal-hidden');
          if (loadingContainers[idx]) {
            loadingContainers[idx].classList.add('terminal-hidden');
          }
        }, 1000); // small delay to avoid flicker when switching between iframes
      });
      container.setAttribute('src', src);
    });
  };

  showError() {
    document.getElementsByName(`loading-container-${this.refName}`).forEach(container => {
      container.parentElement.innerHTML = `<h3 class="air-error">Simulations are currently unavailable. Please login to <a href="${this.air.air_url}" target="_blank">NVIDIA Air</a> or try again later.</h3>`;
    });
  };

  initHandler(el) {
    const self = this;
    el.addEventListener('click', async () => {
      if (!this.id) {
        self.id = await self.air.autoprovision(self);
        if (self.id) {
          self.loadConsoles();
        } else {
          self.showError();
        }
      }
    });
  };
  async launch() {
    if (!this.id) {
      this.id = await this.air.autoprovision(this);
      if (this.id) {
        this.loadConsoles();
      } else {
        this.showError();
      }
    }
  };
}
