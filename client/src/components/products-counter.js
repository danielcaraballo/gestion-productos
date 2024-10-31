class productsCounter extends HTMLElement {
  constructor() {
    super();
    this.innerHTML = /*html*/ `
        <div class="row row-cards">
            <div class="col-12">
                <div id="product-status" class="card">
                    <div class="card-body">
                        <p class="h2">Total de <strong id="total-productos">0</strong> Productos</p>
                        <div class="progress progress-separated mb-3">
                            <div class="progress-bar bg-success" id="barra-operativos" role="progressbar" style="width: 0%;" aria-label="Operativo"></div>
                            <div class="progress-bar bg-azure" id="barra-mantenimiento" role="progressbar" style="width: 0%;" aria-label="Mantenimiento"></div>
                            <div class="progress-bar bg-danger" id="barra-inactivos" role="progressbar" style="width: 0%;" aria-label="Inactivo"></div>
                            <div class="progress-bar bg-primary" id="barra-retirados" role="progressbar" style="width: 0%;" aria-label="Retirado"></div>
                        </div>
                        <div class="row">
                            <div class="col-auto d-flex align-items-center pe-2">
                                <span class="legend me-2 bg-success"></span>
                                <span>Operativo</span>
                            </div>
                            <div class="col-auto d-flex align-items-center px-2">
                                <span class="legend me-2 bg-warning"></span>
                                <span>Mantenimiento</span>
                            </div>
                            <div class="col-auto d-flex align-items-center px-2">
                                <span class="legend me-2 bg-danger"></span>
                                <span>Inactivo</span>
                            </div>
                            <div class="col-auto d-flex align-items-center ps-2">
                                <span class="legend me-2 bg-primary"></span>
                                <span>Retirado</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
          `;
  }
}

customElements.define("products-counter", productsCounter);
