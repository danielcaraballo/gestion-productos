class dependenciesCounter extends HTMLElement {
  constructor() {
    super();
    this.innerHTML = /*html*/ `
        <div class="col-md-6 col-lg-6">
          <div class="card">
            <div class="card-header">
              <h3 class="card-title">Productos por dependencias</h3>
            </div>
            <table class="table card-table table-vcenter">
              <thead>
                <tr>
                  <th>Dependencias</th>
                  <th colspan="2" style="text-align: center">Productos</th>
                </tr>
              </thead>
              <tbody id="dependencias-tbody">
                <!-- Filas generadas dinámicamente aquí -->
              </tbody>
            </table>
          </div>
        </div>
        `;
  }
}

customElements.define("dependencies-counter", dependenciesCounter);
