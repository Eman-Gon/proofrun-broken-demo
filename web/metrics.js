// Deliberately outdated exports. Review metric semantics, not just names.
import { getCLS, getFID, getLCP } from 'web-vitals';

export function collectMetrics(report) {
  getCLS(report);
  getFID(report);
  getLCP(report);
}
